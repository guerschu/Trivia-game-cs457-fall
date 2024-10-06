import selectors



sel = selectors.DefaultSelector()
# while waiting for comms from client
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                # implment accecptWrapper
                print("Accept")
            else:
                # implement service connection
                print("service")
except KeyboardInterrupt:
    print("Service interupted by admin, exiting...")
finally:
    sel.close()
