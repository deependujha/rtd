API Reference
=============

This section contains the complete API documentation for the project.

.. note::
   This is a template API reference. Replace the content below with your actual package documentation.

Core Classes
------------

When you have actual Python modules to document, you can use Sphinx's autodoc feature:

.. code-block:: rst

   .. autoclass:: your_package.YourMainClass
      :members:
      :undoc-members:
      :show-inheritance:

Example Class Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's how you would document a class manually:

**class YourMainClass**

   Main class for handling core functionality.

   **Parameters:**
   
   * **param1** (*str*) -- Description of the first parameter
   * **param2** (*int, optional*) -- Description of the second parameter (default: 0)

   **Methods:**

   .. method:: do_something()

      Performs the main functionality.

      :returns: Result of the operation
      :rtype: str

   .. method:: configure(settings)

      Configures the class with given settings.

      :param dict settings: Configuration dictionary
      :raises ValueError: If settings are invalid

Utility Functions
-----------------

**function process_data(data)**

   Processes input data and returns results.

   :param data: Input data to process
   :type data: list or dict
   :returns: Processed results
   :rtype: dict
   :raises TypeError: If data is not a supported type

**function validate_input(value)**

   Validates input values.

   :param value: Value to validate
   :returns: True if valid, False otherwise
   :rtype: bool

Configuration
-------------

**Environment Variables**

The following environment variables are supported:

.. envvar:: YOUR_PACKAGE_DEBUG

   Enable debug mode when set to ``true`` or ``1``.

.. envvar:: YOUR_PACKAGE_CONFIG_PATH

   Path to the configuration file. Defaults to ``config.yaml``.

.. envvar:: YOUR_PACKAGE_LOG_LEVEL

   Set the logging level. Options: ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``.

**Configuration Options**

.. option:: --verbose, -v

   Enable verbose output.

.. option:: --config <file>

   Specify configuration file path.

.. option:: --output <directory>

   Set output directory for results.

Constants
---------

**DEFAULT_TIMEOUT**
   Default timeout value in seconds (30).

**MAX_RETRIES**
   Maximum number of retry attempts (3).

**SUPPORTED_FORMATS**
   List of supported file formats: ``['json', 'yaml', 'xml']``.
