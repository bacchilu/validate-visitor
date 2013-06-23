# Encapsulating Validation

It's just a simple example of how it's simple encapsulating a validation login inside an object. The code is in validation.py.

Often the result of a validation process cannot be a simple boolean value. Very often we also need an error message and sometimes also an error code.

I think my implementation could be considered a Visitor Design Pattern implementation: actually we iter the argument passed to the validate method (witch returns the boolean result of validation), but we also inspect the final state of the object to recover the error message or error code in necessay, in case of validation error.

Sometime I face the implementation of complex validation logics, and they need a complete set of error messages for the user. I find this solution very comfortable.