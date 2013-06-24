<?

class Validator {

    function Validator(data) {
        $this->data = data;
        $this->errorMsg = NULL;
        $this->errorCode = 0;
        $this->result = true;
    }

    function checkEmpty() {
        if ($this->result === false)
            return;

        if (strlen($this->data) === 0) {
            $this->errorCode = 1;
            $this->errorMsg = "Non può essere vuoto";
            $this->result = false;
            return;
        }
    }

    function checkSize() {
        if ($this->result === false)
            return;

        if (strlen($this->data) < 3) {
            $this->errorCode = 2;
            $this->errorMsg = "Troppo corto";
            $this->result = false;
            return;
        }
        if (strlen($this->data) > 10) {
            $this->errorCode = 3;
            $this->errorMsg = "Troppo lungo";
            $this->result = false;
            return;
        }
    }

    function checkWhitespace() {
        if ($this->result === false)
            return;

        if (preg_match("/\s/", $this->data)) {
            $this->errorCode = 4;
            $this->errorMsg = "Niente spazi";
            $this->result = false;
            return;
        }
    }

    function validate() {
        $this->checkEmpty();
        $this->checkSize();
        $this->checkWhitespace();
        return $this->result;
    }
}

?>