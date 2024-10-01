from typing import Callable
from __future__ import annotations

class Event:
  type Listener[T] = Callable[[T, Event.Context], None]

  class Context:
    def __init__(self, tree, node, kind, path):
      self.tree = tree
      self.node = node
      self.kind = kind
      self.path = path

  class Tree:
    __LISTEN_ACTION__ = "listen"
    __DEAFEN_ACTION__ = "deafen"
    __ATTACH_ACTION__ = "attach"
    __DETACH_ACTION__ = "detach"
    __DELETE_ACTION__ = "delete"

    def __init__(self):
      self.root = Event.Node()

      self.queue = [ ]

    def listen[T](self, kind: str, listener: Event.Listener[T] = None, path: str = "", defer: bool = True):
      a = { "action": Event.Tree.__LISTEN_ACTION__, "kind": kind, "listener": listener, "path": path }
      if defer or defer == None:
        self._queue(a)
      else:
        self._flush(a)

    def deafen[T](self, kind: str, listener: Event.Listener[T] = None, path: str = "", defer: bool = True):
      a = { "action": Event.Tree.__DEAFEN_ACTION__, "kind": kind, "listener": listener, "path": path }
      if defer or defer == None:
        self._queue(a)
      else:
        self._flush(a)

    def attach(self, path: str, defer: bool = True):
      a = { "action": Event.Tree.__ATTACH_ACTION__, "path": path }
      if defer or defer == None:
        self._queue(a)
      else:
        self._flush(a)

    def detach(self, path: str, defer: bool = True):
      a = { "action": Event.Tree.__DETACH_ACTION__, "path": path }
      if defer or defer == None:
        self._queue(a)
      else:
        self._flush(a)

    def delete(self, path: str, defer: bool = True):
      a = { "action": Event.Tree.__DELETE_ACTION__, "path": path }
      if defer or defer == None:
        self._queue(a)
      else:
        self._flush(a)

    def poll(self):
      _queue = self.queue[::]         # clone queue
      self.queue[::]  =  [  ]         # clear queue
      for a in _queue: self._flush(a) # flush queue

    def _queue(self, a):
      self.queue.append(a)

    def _flush(self, a):
      match a.action:
        case Event.Tree.__LISTEN_ACTION__: self._on_listen(a)
        case Event.Tree.__DEAFEN_ACTION__: self._on_deafen(a)
        case Event.Tree.__ATTACH_ACTION__: self._on_attach(a)
        case Event.Tree.__DETACH_ACTION__: self._on_detach(a)
        case Event.Tree.__DELETE_ACTION__: self._on_delete(a)

    def _on_listen(self, a):
      Event.Node._require(self.root, a.path)

    def _on_deafen(self, a):
      pass

    def _on_attach(self, a):
      pass

    def _on_detach(self, a):
      pass

    def _on_delete(self, a):
      pass





  class Node:
    def __init__(self):
      self.children  = { }
      self.listeners = { }

    def _request_node(root, path: str):
      for part in path.split("."):
        if part in root.children:
          root = root.children[part]
        else:
          return None
      return root

    def _require_node(root, path: str):
      for part in path.split("."):
        if part in root.children:
          root = root.children[part]
        else:
          root = root.children[part] = Event.Node()
      return root
    
    def _request_listeners(node, kind: str) -> list[Callable]:
      pass

    def _require_listeners(node, kind: str) -> list[Callable]:
      pass


