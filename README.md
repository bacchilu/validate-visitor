# Encapsulating Validation

It's just a simple example of how it's simple encapsulating a validation login inside an object. The code is in validation.py.

Often the result of a validation process cannot be a simple boolean value. Very often we also need an error message and sometimes also an error code.

I think my implementation could be considered a Visitor Design Pattern implementation: actually we iter the argument passed to the validate method (witch returns the boolean result of validation), but we also inspect the final state of the object to recover the error message or error code in necessay, in case of validation error.

Sometime I face the implementation of complex validation logics, and they need a complete set of error messages for the user. I find this solution very comfortable.

# Why don't you better use exceptions?

Of course I could encapsulate both errorMsg and errorCode inside the ValidatorException object and then raise an instance of it.

Actually I have to admit that I moved to this solution coding in PHP4 witch does not support exceptions, so I had no choice.

Anyway I have also to say that in this way I can only expose to a client only the Validator object: the ValidatorException object doesn't need to be visible outside the validation module.

I also like the idea of 'keeping all together': validation logic and validation result informations are all inside the same class.