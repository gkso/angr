import angr

######################################
# std::throw_length_error
######################################

class std____throw_logic_error(angr.SimProcedure): #pylint:disable=redefined-builtin
    #pylint:disable=arguments-differ

    NO_RET = True
    __altnames__ = ('std::__throw_length_error(char const*)', )

    def run(self):
        # FIXME: we need the concept of C++ exceptions to implement this right
        self.exit(1)