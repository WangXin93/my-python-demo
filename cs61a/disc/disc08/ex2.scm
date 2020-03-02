; Q3.1
; False
; True
; True
; True

; Q3.2
(define (fib n)
 (define (fib-sofar a b n)
  (if (> n 0)
   (fib-sofar b (+ a b) (- n 1))
   a))
 (fib-sofar 0 1 n)
)

; Q3.3
(define (sum lst)
 (define (sum-sofar lst s)
  (if (null? lst)
   s
   (sum-sofar (cdr lst) (+ s (car lst))))
 )
 (sum-sofar lst 0)
)

; Q3.4
; a)
(define (reverse lst)
 (define (reverse-sofar lst lst-sofar)
  (if (null? lst) lst-sofar
   (reverse-sofar (cdr lst) (cons (car lst) lst-sofar)))
 )
 (reverse-sofar lst nil)
)

; b)
(define (append a b)
 (define (rev-append-tail a b)
  (if (null? a) b
   (rev-append-tail (cdr a) (cons (car a) b)))
 )
 (rev-append-tail (reverse a) b)
)

; c)
(define (insert n lst)
 (define (rev-insert lst rev-lst)
  (cond ((null? lst) rev-lst)
        ((> (car lst) n) (append (reverse lst) (cons n rev-lst)))
        (else (rev-insert (cdr lst) (cons (car lst) rev-lst))))
 )
 (reverse (rev-insert lst nil))
)
