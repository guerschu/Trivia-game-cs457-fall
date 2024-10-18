import sys
import selectors
import json
import io
import struct


class Messages:
    def __init__(self, selector, sock, addr, request):
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self.request = request
        self._recv_buffer = b""
        self._send_buffer = b""
        self._request_queued = False
        self._jsonheader_len = None
        self.jsonHeader = None
        self.response = None

def _setSelectorEventsMask(self, mode):
        """Set selector to listen for events: mode is 'r', 'w', or 'rw'."""
        if mode == "r":
            events = selectors.EVENT_READ
        elif mode == "w":
            events = selectors.EVENT_WRITE
        elif mode == "rw":
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
        else:
            raise ValueError(f"Invalid events mask mode {repr(mode)}.")
        self.selector.modify(self.sock, events, data=self)    

def _read(self):
    try:
        data = self.sock.recv(4096) # this could be subject to change
    except BlockingIOError:
        pass
    else:
        if data:
            self._recv_buffer += data
        else:
            raise RunTimeError("Peer is closed.")

def _write(self):
    print("sending", repr(self._send_buffer), "to", self.addr)
    try:
        sent = self.sock(self._send_buffer)
    except BlockIOError:
        pass
    else:
        self._send_buffer = self._send_buffer[sent:]

def _jsonEncode(self, obj, encoding):
    return json.dumps(obj, ensure_ascii=False).encode(encoding)

def jsonDecode(self, json_bytes, encoding):
    tiowForSomeReason = io.TextIOWrapper(io.BytesIO(json_bytes), encoding=encoding, newline="")
    obj = json.load(tiowForSomeReason)
    tiowForSomeReason.close()
    return obj

def _createMessage(self, contenBytes, contentType, contentEncoding):
    jsonHeader = {
        "byteorder": sys.byteorder,
        "content-type": contentType,
        "content-encoding": contentEncoding,
        "content-length": len(contenBytes),
    }
    jsonHeaderBytes = self._jsonEncode(jsonHeader, "utf-8")
    messageHDR = struct.pack(">H", len(jsonHeaderBytes))
    message = messageHDR + jsonHeaderBytes + contenBytes
    return message

def _processResponseJsonContent(self):
    content = self.response
    result = content.get("result")
    print(f"got the results: {result}")

def process_events(self, mask):
    if mask & selectors.EVENT_READ:
        self.read()
    if mask & selectors.EVENT_WRITE:
        self.write()

def read(self):
    self._read()

    if self._jsonheader_len is None:
        self.processProtoheader()

    if self._jsonheader_len is not None:
        if self.jsonHeader is None:
            self.process_jsonheader()

    if self.jsonHeader:
        if self.response is None:
            self.process_response()

def write(self):
        if not self._request_queued:
            self.queue_request()

        self._write()

        if self._request_queued:
            if not self._send_buffer:
                # Set selector to listen for read events, we're done writing.
                self._set_selector_events_mask("r")

def close(self):
    print("closing connection to", self.addr)
    try:
        self.selector.unregister(self.sock)
    except Exception as e:
        print(
            f"error: selector.unregister() exception for",
            f"{self.addr}: {repr(e)}",
        )

    try:
        self.sock.close()
    except OSError as e:
        print(
            f"error: socket.close() exception for",
            f"{self.addr}: {repr(e)}",
        )
    finally:
        # Delete reference to socket object for garbage collection
        self.sock = None

def queue_request(self):
    content = self.request["content"]
    centextType = self.request["type"]
    contextEncoding = self.request["encoding"]
    if contentType == "text/json":
        req = {
            "context_bytes": self._jsonEncode(content, contentEncoding),
            "content_type": contentType,
            "content_encoding": contentEncoding,
        }
    else:
        req = {
            "context_bytes": content,
            "content_type": contentType,
            "content_encoding": contentEncoding,
        }
    message = self._createMessage(**req)
    self._send_buffer +=message
    self._request_queued = True

def processProtoheader(self):
    hdrlen = self._jsonheader_len
    if len(self._recv_buffer) >= hdrlen:
        self.jsonHeader = self._jsonDecode(self._recv_buffer[:hdrlen], "utf-8")
        self._recv_buffer = self._recv_buffer[hdrlen:]
        for reqhdr in ("byteorder","content-length","content-type","content-encoding"):
            if reqhdr not in self.jsonHeader:
                raise ValueError(f'Missing required header: "{reqhdr}".')

def process_response(self):
    contentLen = self.jsonHeader["content-length"]
    if not len(self._recv_buffer) >= contentLen:
        return
    data = self._recv_buffer[:contentLen]
    self._recv_buffer = self._recv_buffer[contentLen:]
    if self.jsonHeader["content-type"] == "text/json":
        encoding = self.jsonHeader["content-encoding"]
        self.response = self._jsonDecode(data, encoding)
        print("recieved response", repr(self.response), "from", self.addr)
        self._processResponseJsonContent()
    else:
        self.response = data
        print(f'recieved {self.jsonHeader["content-type"]} response from', self.addr)
        self._processResponseJsonContent()
    self.close()


