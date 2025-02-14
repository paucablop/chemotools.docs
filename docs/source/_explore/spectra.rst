.. _spectra:

**Working with Single Spectra in Scikit-learn**
================================================

When working with spectroscopic data in ``scikit-learn``, you often need to reshape single spectra to fit the expected data shapes. This guide explains how to reshape single spectra for preprocessing in ``scikit-learn`` and ``chemotools``.

Understanding Data Shapes
-------------------------

While ``scikit-learn`` preprocessing techniques expect 2D arrays (matrices) where:

* Each row represents a sample
* Each column represents a feature

spectroscopic data often comes as single spectra in 1D arrays (vectors). Here's an example of a single spectrum:

.. code-block:: python

    array([0.484434, 0.485629, 0.488754, 0.491942, 0.489923, 0.492869,
           0.497285, 0.501567, 0.500027, 0.50265])

Reshaping for Preprocessing
---------------------------

To use ``scikit-learn`` and ``chemotools`` with single spectra, you need to reshape the 1D array into a 2D array with one row. Here's how:

.. code-block:: python

    import numpy as np
    from chemotools.scatter import MultiplicativeScatterCorrection

    msc = MultiplicativeScatterCorrection()
    spectra_msc = msc.fit_transform(spectra.reshape(1, -1))

The ``reshape(1, -1)`` method converts the 1D array ``spectra`` into a 2D array with a single row. The result looks like this:

.. code-block:: python

    array([[0.484434, 0.485629, 0.488754, 0.491942, 0.489923, 0.492869,
            0.497285, 0.501567, 0.500027, 0.50265]])

.. note::
   The reshaped output is a 2D array with a single row - the format required by 
   ``scikit-learn`` and ``chemotools`` preprocessing techniques.