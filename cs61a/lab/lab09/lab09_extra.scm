;; Extra Scheme Questions ;;


; Q5
(define lst
   (list (list 1) 2 (cons 3 4) 5)
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (if (null? lst) lst
   (if (= item (car lst)) (remove item (cdr lst))
    (cons (car lst) (remove item (cdr lst))))
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond
   ((zero? (min a b)) (max a b))
   ((< a b) (gcd b a))
   ((= (remainder a b) 0) b)
   (else (gcd b (remainder a b)))
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (null? s) s
   (cons (car s) (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s))))
  )
)

; Q10
(define (substitute s old new)
 (if (null? s) s
  (cons (if (pair? (car s)) (substitute (car s) old new)
             (if (eq? (car s) old) new (car s)))
   (substitute (cdr s) old new))
  )
)

; Q11
(define (sub-all s olds news)
 (if (null? olds) s
  (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
 )
)
