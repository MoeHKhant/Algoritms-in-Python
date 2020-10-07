import numpy as np
from qiskit.aqua import MissingOptionalLibraryError
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def breast_cancer(training_size, test_size, n, plot_data=False):
    """ returns breast cancer dataset """
    class_labels = [r"A", r"B"]
    data, target = datasets.load_breast_cancer(return_X_y=True)
    sample_train, sample_test, label_train, label_test = train_test_split(
        data, target, test_size=0.3, random_state=12
    )

    # Now we standardize for gaussian around 0 with unit variance
    std_scale = StandardScaler().fit(sample_train)
    sample_train = std_scale.transform(sample_train)
    sample_test = std_scale.transform(sample_test)

    # Now reduce number of features to number of qubits
    pca = PCA(n_components=n).fit(sample_train)
    sample_train = pca.transform(sample_train)
    sample_test = pca.transform(sample_test)

    # Scale to the range (-1,+1)
    samples = np.append(sample_train, sample_test, axis=0)
    minmax_scale = MinMaxScaler((-1, 1)).fit(samples)
    sample_train = minmax_scale.transform(sample_train)
    sample_test = minmax_scale.transform(sample_test)

    # Pick training size number of samples from each distro
    training_input = {
        key: (sample_train[label_train == k, :])[:training_size]
        for k, key in enumerate(class_labels)
    }
    test_input = {
        key: (sample_test[label_test == k, :])[:test_size]
        for k, key in enumerate(class_labels)
    }

    if plot_data:
        try:
            import matplotlib.pyplot as plt
        except ImportError as ex:
            raise MissingOptionalLibraryError(
                libname="Matplotlib",
                name="breast_cancer",
                pip_install="pip install matplotlib",
            ) from ex
        for k in range(0, 2):
            plt.scatter(
                sample_train[label_train == k, 0][:training_size],
                sample_train[label_train == k, 1][:training_size],
            )

        plt.title("PCA dim. reduced Breast cancer dataset")
        plt.show()

    return sample_train, training_input, test_input, class_labels
