WAP SYS V -- CRE section
---
This section has the code for the CRE (Common Runtime Engine) section.

This section has the necessary code to achieve Independence on the underlying engine and its particularities

This section is composed of the following parts:

 * **core**  --  This module implements the base class / package under which posterior modules are loaded
    * **security**  --  This module implements then security layer, accessing the relevant sub-systems on the back end layer
        * **SAM**  (Security Access Manager)  --  This module implements the functions to validate credentials
        * **ACL**   (Access Control Lists)  --  This module implements the functions to verify / validate accessing rights
    * **code_start**  --  This module implements the global functions and data structures for code start-up and code shutdown
    * **code_init**  -- This module implements the global functions and data structures for code initialization (performed module by module, after module initial loading), and loads the **init** module
    * **init**  -- This module is loaded by the **code_init** module and is responsible by the loadding and registration of all subsequente CRE modules. After all are loaded, it calls the necessary functions at the **code_start** module to perform the **COLD_START** action of all **CRE** modules and, afterwards, it calls the necessary functions  at **code_init** to perform the **INITIALIZATION** action of all **CRE** modules.
        * **debug_logger**  --  This module implements the _syslog_ access interface and _log instance container_ for all defined _log channels_, the load of the **debug_logging** module and any existing **Log-x** _log channel_ definition module
            * **debug_logging**  --  This module implements the **DEBUG** and **LOG** functions
            * **Log-1**  --  _Log channel_ 'Log-1' definition and instancialization module
            * **Log-2**  --  _Log channel_ 'Log-2' definition and instancialization  module
            *  ....
            * **Log-n**  --  _Log channel_ 'Log-n' definition and instancialization module
        * **code_runner**  -- This module implements the _code_runner_ execution layer, that abstracts from the underlying existing features
            * **exception_handlers**  --  This module implements / defines _exception handlers_ for exception's processing
                * **ULS_exceptions**  --  This module implements the functions to register ULS exceptions, each one defined in it's own file, automatically loaded if present in the right directory
                * **ULS_handlers**  --  This module implements the functions to register ULS exception handlers, each one defined in it's own file, automatically loaded if present in the right directory
            * **runtime_engine**  --  This module implements the interface with the _runtime engine_
                * **code_interrupts**  --  This module implements the _code interrupts_ which are used for timing purpouses and multi processing
                * **code_scheduler**  --  This module implements the _code scheduler_ (both for threads and processes)
                * **code_threads**  --  This module implements the _thread's interface_ and the _code threads_
                * **code_processes**  --  This module implements the _process interface_ and the _code processes_
                * **code_interpreters**  --  This module implements the _generic interpreter interface_ and any specific _code interpreters_, with each one implemented in it's own file, automatically loaded if present in the right directory
        * **error_handler**  --  This module implements the error handling infrastructure and _error frame_ data structures
            * **bootstrap**  --  This module implements the _bootstrap_ code, which loads the modules presente in the appropriated directory
                * **app_args**  --  This module implements the code to retrive any passed parameters, regardless the way the code was invoked, storing them in the appropriated data structures
                * **p_state**  --  This module implements the _code state save/reload infrastructure
                    * **p_session**  --  This module implements the _presentation session_ code
                        * **base_static_class**  --  This module implements a base static class for subsequent use
                        * **base data_class**  --  This module implements a base data container class for subsequent use
                        * **base_std_class**  --  This module implements a base standard (instantiable) class for subsequent use
                * **static_config**  --  This module implements the code to read, parse and decode the static configuration files
                * **toolbox**  --  This module implements the _toolbox_ interface and initialize all _toolbox componentes_, loaded automatically from the appropriate directory
                * **app_engines**  --  This module implements the interface and registration service for the existing 'app_engines', loaded automatically from the appropriated directory
                    * **app-engine-1**  --  This module implements the **app-engine-1** interface code
                    * **app-engine-2**  --  This module implements the **app-engine-2** interface code
                    *   ....
                    * **app-engine-n**  --  This module implements the **app-engine-n** interface code
                * **arg_parser**  --  This module implements the code to parse the passed arguments and determine, in other things, which _application_ was called
            * **boot_loader**  --  This module implements the code to read the _application configuration file_ and to load and initialize all required modules / code to run the sellected _application_

 