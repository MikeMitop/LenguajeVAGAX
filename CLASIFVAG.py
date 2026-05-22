# librerias/CLASIFVAG.py
# Clasificación para VAGAX — CERO imports nativos
from librerias.MATHVAG import MATHVAG


class CLASIFVAG:

    @staticmethod
    def _distancia(a, b):
        s = 0
        for i in range(len(a)):
            s += (a[i] - b[i]) ** 2
        return MATHVAG.sqrt(s)

    @staticmethod
    def knn_classify(X_train, y_train, x_new, k):
        n = len(X_train)
        dists = []
        for i in range(n):
            d = CLASIFVAG._distancia(X_train[i], x_new)
            dists.append((d, y_train[i]))
        for i in range(len(dists)):
            for j in range(0, len(dists) - i - 1):
                if dists[j][0] > dists[j+1][0]:
                    dists[j], dists[j+1] = dists[j+1], dists[j]
        votos = {}
        for i in range(k):
            l = dists[i][1]
            votos[l] = votos.get(l, 0) + 1
        best = None
        best_c = -1
        for l in votos:
            if votos[l] > best_c:
                best_c = votos[l]
                best = l
        return best

    @staticmethod
    def knn_predict(X_train, y_train, X_test, k):
        return [CLASIFVAG.knn_classify(X_train, y_train, x, k) for x in X_test]

    @staticmethod
    def knn_accuracy(X_train, y_train, X_test, y_test, k):
        preds = CLASIFVAG.knn_predict(X_train, y_train, X_test, k)
        c = 0
        for i in range(len(y_test)):
            if preds[i] == y_test[i]: c += 1
        return c / len(y_test) if y_test else 0

    @staticmethod
    def _gini(labels):
        if not labels: return 0
        n = len(labels)
        counts = {}
        for l in labels:
            counts[l] = counts.get(l, 0) + 1
        g = 1.0
        for c in counts:
            p = counts[c] / n
            g -= p * p
        return g

    @staticmethod
    def _majority(labels):
        counts = {}
        for l in labels:
            counts[l] = counts.get(l, 0) + 1
        best = None
        best_c = -1
        for l in counts:
            if counts[l] > best_c:
                best_c = counts[l]
                best = l
        return best

    @staticmethod
    def _best_split(X, y):
        n = len(X)
        if n == 0: return None, None
        nf = len(X[0])
        best_g = float('inf')
        best_f = None
        best_t = None
        for f in range(nf):
            vals = list(set(X[i][f] for i in range(n)))
            vals = MATHVAG._sort(vals)
            for ti in range(len(vals) - 1):
                t = (vals[ti] + vals[ti+1]) / 2
                ly, ry = [], []
                for i in range(n):
                    if X[i][f] <= t: ly.append(y[i])
                    else: ry.append(y[i])
                if not ly or not ry: continue
                g = (len(ly)/n)*CLASIFVAG._gini(ly) + (len(ry)/n)*CLASIFVAG._gini(ry)
                if g < best_g:
                    best_g = g
                    best_f = f
                    best_t = t
        return best_f, best_t

    @staticmethod
    def decision_tree_fit(X, y, max_depth=5, depth=0):
        unique = list(set(y))
        if len(unique) == 1:
            return {"leaf": True, "class": unique[0]}
        if depth >= max_depth or len(X) <= 1:
            return {"leaf": True, "class": CLASIFVAG._majority(y)}
        f, t = CLASIFVAG._best_split(X, y)
        if f is None:
            return {"leaf": True, "class": CLASIFVAG._majority(y)}
        lX, ly, rX, ry = [], [], [], []
        for i in range(len(X)):
            if X[i][f] <= t:
                lX.append(X[i]); ly.append(y[i])
            else:
                rX.append(X[i]); ry.append(y[i])
        if not lX or not rX:
            return {"leaf": True, "class": CLASIFVAG._majority(y)}
        return {
            "leaf": False, "feature": f, "threshold": t,
            "left": CLASIFVAG.decision_tree_fit(lX, ly, max_depth, depth+1),
            "right": CLASIFVAG.decision_tree_fit(rX, ry, max_depth, depth+1)
        }

    @staticmethod
    def decision_tree_predict(tree, x):
        if tree["leaf"]: return tree["class"]
        if x[tree["feature"]] <= tree["threshold"]:
            return CLASIFVAG.decision_tree_predict(tree["left"], x)
        return CLASIFVAG.decision_tree_predict(tree["right"], x)

    @staticmethod
    def decision_tree_predict_batch(tree, X):
        return [CLASIFVAG.decision_tree_predict(tree, x) for x in X]

    @staticmethod
    def confusion_matrix(y_true, y_pred):
        labels = MATHVAG._sort(list(set(y_true + y_pred)))
        n = len(labels)
        idx = {}
        for i in range(n): idx[labels[i]] = i
        mat = [[0]*n for _ in range(n)]
        for i in range(len(y_true)):
            mat[idx[y_true[i]]][idx[y_pred[i]]] += 1
        return mat, labels

    @staticmethod
    def accuracy(y_true, y_pred):
        if not y_true: return 0
        c = 0
        for i in range(len(y_true)):
            if y_true[i] == y_pred[i]: c += 1
        return c / len(y_true)

    @staticmethod
    def precision(y_true, y_pred, positive=1):
        tp = fp = 0
        for i in range(len(y_true)):
            if y_pred[i] == positive:
                if y_true[i] == positive: tp += 1
                else: fp += 1
        return tp / (tp + fp) if (tp + fp) > 0 else 0

    @staticmethod
    def recall(y_true, y_pred, positive=1):
        tp = fn = 0
        for i in range(len(y_true)):
            if y_true[i] == positive:
                if y_pred[i] == positive: tp += 1
                else: fn += 1
        return tp / (tp + fn) if (tp + fn) > 0 else 0

    @staticmethod
    def f1_score(y_true, y_pred, positive=1):
        p = CLASIFVAG.precision(y_true, y_pred, positive)
        r = CLASIFVAG.recall(y_true, y_pred, positive)
        if p + r == 0: return 0
        return 2 * p * r / (p + r)

    @staticmethod
    def classification_report(y_true, y_pred):
        labels = MATHVAG._sort(list(set(y_true + y_pred)))
        print("\n" + "=" * 50)
        print("  CLASSIFICATION REPORT")
        print("=" * 50)
        for label in labels:
            p = CLASIFVAG.precision(y_true, y_pred, label)
            r = CLASIFVAG.recall(y_true, y_pred, label)
            f = CLASIFVAG.f1_score(y_true, y_pred, label)
            print(f"  {str(label):<10} P={p:.4f}  R={r:.4f}  F1={f:.4f}")
        acc = CLASIFVAG.accuracy(y_true, y_pred)
        print(f"  Accuracy: {acc:.4f}")
        print("=" * 50 + "\n")

    @staticmethod
    def kmeans(X, k, max_iter=100):
        """K-Means clustering. Returns [labels, centroids]"""
        n = len(X)
        dims = len(X[0])
        centroids = [X[i][:] for i in range(k)]
        labels = [0] * n
        for _ in range(max_iter):
            new_labels = []
            for i in range(n):
                min_d = float('inf')
                best = 0
                for c in range(k):
                    d = CLASIFVAG._distancia(X[i], centroids[c])
                    if d < min_d:
                        min_d = d
                        best = c
                new_labels.append(best)
            changed = False
            for i in range(n):
                if new_labels[i] != labels[i]:
                    changed = True
                    break
            labels = new_labels
            if not changed:
                break
            for c in range(k):
                sums = [0.0] * dims
                count = 0
                for i in range(n):
                    if labels[i] == c:
                        count += 1
                        for d in range(dims):
                            sums[d] += X[i][d]
                if count > 0:
                    for d in range(dims):
                        centroids[c][d] = sums[d] / count
        return [labels, centroids]
