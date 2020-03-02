; Q1
(define pi 3.14)
pi
'pi
(if 2 3 4)
(if 0 3 4)
(if #f 3 4)
(if nil 3 4)
(if (- 1 1) 'hello 'goodbye)
(define (factorial n)
 (if (= n 0) 
  1
  (* n (factorial (- n 1))))
)
(factorial 5)
(= 2 3)
(= '() '())
(eq? '() '())
(eq? nil nil)
(eq? '() nil)
(pair? (cons 1 2))
(list? (cons 1 2))

; Q2
(define (hailstone seed n)
 (cond
  ((= n 0) seed)
  ((even? seed) (hailstone (quotient seed 2) (- n 1)))
  (else (hailstone (+ (* seed 3) 1) (- n 1))))
)

; Q4
(define (well-formed s)
 (cond
  ((null? s) #t)
  ((number? (cdr s)) #f)
  (else (well-formed (cdr s)))
 )
)

; Q5
(define (is-prefix p lst)
 (cond 
  ((null? p) #t)
  ((not (eq? (car p) (car lst))) #f)
  (else (is-prefix (cdr p) (cdr lst))))
)

; scm> (is-prefix '() '())
; #t
; scm> (is-prefix '() '(1 2 3))
; #t
; scm> (is-prefix '(1) '(1 2 3))
; #t
; scm> (is-prefix '(1 2) '(1 2 3))
; #t

