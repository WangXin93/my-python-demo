; Q1
(define (compose-all funcs)
  (if (null? funcs)
    (lambda (x) x)
    (lambda (x) ((compose-all (cdr funcs))
                 ((car funcs) x)))
  )
)

(define (square x) (* x x))
(define (add-one x) (+ x 1))
(define (double x) (* x 2))
(define composed (compose-all (list double square add-one)))

; Q2
(define (tail-replicate x n)
  (define (helper left head)
    (if (= left 0) head
      (helper (- left 1) (cons x head))
    )
  )
  (helper n nil)
)

(tail-replicate 3 10)