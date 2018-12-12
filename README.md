# verify-protocol
An interactive tool for Secure Distributed Computer Systems

This tool helps in designing protocols and verifying their security using Python3. It uses principles of the Readers-Writers Flow Model(RWFM) to achieve this. It supports two processing modes - manual and process-from-file.

Maunal Mode: In manual mode, first you have provide the names of the participating principals, and the initial objects and their labels. Then you enter the steps one by one and the tool informs the change in state and whether it a secure step or not. If the step is not secure, it does not allow the step to execute and informs the user about the security issue.

Process-from-file Mode: In process-from-file mode, the tool directly processes from the file provided by the user. It informs the user about the actions taken after every step that is present in the file. The security concerns of the protocol is handled in the same way as that in manual mode. When the end of the file is reached, it shifts to manual mode.

At any point if the user does not want to enter any further steps, he/she should enter “exit” to stop the execution. For every complete execution of the code, 2 files are created. One is the protocol file from which we can later process and the other is a detailed IFD of the protocol.

Verification of 3 predefined protocols, Needham-Schroeder Protocol, Gong’s Protocol and TMN Protocol is done. Also a new protocol is designed and verified.
