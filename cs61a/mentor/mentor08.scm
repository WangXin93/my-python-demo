; Q1
(define (count-instance lst x)
  (cond ((null? lst) 0)
        ((equal? (car lst) x) (+ 1 (count-instance (cdr lst) x)))
        (else (count-instance (cdr lst) x)))
)

(define (count-tail-helper lst x cnt)
  (cond ((null? lst) cnt)
        ((equal? (car lst) x) (count-tail-helper (cdr lst) x (+ 1 cnt)))
        (else (count-tail-helper (cdr lst) x cnt))
  )
)

(define (count-tail lst x)
  (count-tail-helper lst x 0)
)

; Q2
(define (filter f lst)
  (cond ((null? lst) lst)
        ((f (car lst)) (cons (car lst) (filter f (cdr lst))))
        (else (filter f (cdr lst))))
)

(define (filter-tail f lst)
  (define (filter-reverse lst res)
    (cond ((null? lst) res)
          ((f (car lst)) (filter-reverse (cdr lst) (cons (car lst) res)))
          (else (filter-reverse (cdr lst) res))
    )
  )
  (reverse (filter-reverse lst '()))
)

(define (reverse s)
  (define (reverse-iter s r)
    (if (null? s) r
      (reverse-iter (cdr s) (cons (car s) r))
    )
  )
  (reverse-iter s '())
)
