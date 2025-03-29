- _Java inheritance_ refers to the ability in Java for one class to inherit from another class. In Java this is also called extending a class. One class can _extend_ another class and thereby _inherit_ from that class.

- When one class inherits from another class in Java, the two classes take on certain roles. The class that extends (inherits from another class) is the _subclass_ and the class that is being extended (the class being inherited from) is the _superclass_ . In other words, the subclass extends the superclass.

- When a class inherits from a superclass, it inherits parts of the superclass methods and fields. The subclass can also override (redefine) the inherited methods. Fields cannot be overridden, but can be "shadowed" in subclasses. How all this works is covered later in this text.

- You can always cast an object of a subclass to one of its superclasses. This is referred to as _upcasting_ (from a subclass type to a superclass type).

It may also be possible to cast an object from a superclass type to a subclass type, but only if the object really is an instance of that subclass (or an instance of a subclass of that subclass). This is referred to as _downcasting_ (from a superclass type to a subclass type). Thus, this example of downcasting is valid:
Still inhertance and nested class pending
