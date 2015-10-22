WAP SYS V -- IPL section
---
This section has the code for the IPL (Initial Program Load) section.

This section is composed of the following parts:

 * data_class
    * This module implements a base data container model
 * std_class
    * This module implements a base instatiable class model
 * static_class
    * This module implements a base static class model (to be used as na infrastructure element)
 * BESSAM (Back End Sub-System Access Manager)
    * This module implements the connection / communication element with the background Back End Sub System (which implements the ROOT Server, SAM and ACL services)
 * sys_log
    * This module implements simple and early logging functions
 * code_loader
    * This module implements the CODE_LOADER used to load all subsequente modules, starting on the CORE module, the parente module on the CRE (Common Runtime Engine)
    