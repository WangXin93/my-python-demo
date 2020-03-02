(define (length s)
  (if (null? s)
     0
     (+ 1 (length (cdr s)))))
