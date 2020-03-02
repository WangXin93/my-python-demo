; Q1
(cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 5)) (cons 6 nil))))

(cons (cons (car '(1 2 3)) (list 2 4 5)) (cons 2 3))

(define a 4)
((lambda (x y) (+ a)) 1 2)

((lambda (x y z) (y x)) 2 / 2)

((lambda (x) (x x)) (lambda (y) 4))

(define boom1 (/ 1 0))

boom1

(define boom2 (lambda () (/ 1 0)))

(boom2)

(define (boom3) (/ 1 0))

(boom3)

; Q2
(if 0 (/ 1 0) 1)

(and 1 #f (/ 1 0))

(and 1 2 3)

(or #f #f 0 #f (/ 1 0))

(or #f #f (/ 1 0) 3 4)

(and (and) (or))

; Q3
(let ((x 1)) (+ x 1))

((lambda (x) (+ x 1)) 1)

;(let ((foo 3) (bar (+ foo 2))) (+ foo bar))
(let ((foo 3)) (+ foo (+ foo 2)))
((lambda (foo) (+ foo (+ foo 2))) 3)

;;;;;;;;;;; Code-Writing ;;;;;;;;;;;;;
;Q1
(define (waldo lst)
  (if (null? lst) #f
    (if (eq? (car lst) 'waldo) #t
      (waldo (cdr lst)))
  )
)
(waldo '(1 4 waldo))
(waldo '())
(waldo '(1 4 9))

;Q2
(define (waldo lst)
  (if (null? lst) #f
    (if (eq? (car lst) 'waldo) 0
      (if (waldo (cdr lst)) (+ 1 (waldo (cdr lst))) #f)
    )
  )
)
(define (waldo lst)
  (if (null? lst) #f
    (if (eq? (car lst) 'waldo) 0
      (let ((has (waldo (cdr lst)))) (if has (+ 1 has) #f))
    )
  )
)
(waldo '(1 4 waldo))
(waldo '())
(waldo '(1 4 9))

; Q3
(define (quicksort lst)
  (if (< (length lst) 2) lst
      (let ((pivot (car lst)))
        (append (quicksort (filter (lambda (x) (< x pivot)) lst))
                (list pivot)
                (quicksort (filter (lambda (x) (> x pivot)) lst))
        )
      )
  )
)
(quicksort (list 5 2 4 3 12 7))


