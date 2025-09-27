Quick start
===========

Check the `installation guide <../_user/install.html>`_ to get started.

.. hint::
    **New in chemometrics?** Check it out in our fully fledged tutorials `here <../_learn/index.html>`_.

.. hint::
    **Want to discover the environment at your hands?** Check it out our exploration page `here <../_explore/index.html>`_.

Load example data
-----------------

This loads a training set of mid infrared spectra (``X_train``) and associated reference values (``y_train``) from a fermentation process.

.. code-block:: python

    from chemotools.datasets import load_fermentation_train

    X_train, y_train = load_fermentation_train()

.. hint::
    **Want to know more about available datasets?** Check it out our datasets `here <../_learn/datasets.html>`_.

Preprocess the data
-------------------

Load, define and apply preprocessing steps to the training data. Here we use a Savitzky-Golay filter to compute the first derivative of the sample spectra.

.. code-block:: python

    from chemotools.derivate import SavitzkyGolay

    # Configure the preprocessing step
    sg = SavitzkyGolay(window_size=3, polynomial_order=1, derivate_order=1)

    # Fit and transform the training data
    X_train_preprocessed = sg.fit_transform(X_train)

.. hint::
    **Want to know more about available preprocessing methods?** Check it out our preprocessings `here <../_methods/index.html>`_.

Compose preprocessings and models
---------------------------------

Combine preprocessing and modelling steps in a single pipeline. 

.. code-block:: python

    from chemotools.derivate import SavitzkyGolay
    from sklearn.cross_decomposition import PLSRegression
    from sklearn.pipeline import make_pipeline
    

    # Define the pipeline
    pipeline = make_pipeline(
        SavitzkyGolay(window_size=3, polynomial_order=1, derivate_order=1),
        PLSRegression(n_components=2)
    )

    # Fit the pipeline to the training data
    pipeline.fit(X_train, y_train)

.. hint::
    **Want to know more about pipelines?** Check it out our pipelines `here <../_explore/pipelines.html>`_.

.. hint::
    **Want to know more about how to optimize your models?** Check it out optimization techniques `here <../_explore/optiimize.html>`_.