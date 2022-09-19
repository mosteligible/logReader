# logReader

A system design problem that requires designing a logging service.
It consists of client ends that subscribe to this logging service to save their logs. This logging service provides a way for clients to send their logs as they are generated.

The system consists of three parts to function.

1. A receiver to receive logs from clients.
2. A handler/parser to get logs received from clients to right format/structure to save.
3. A storage system to save the logs passed on by clients that also provides a way to acces the logs at later point in time.
