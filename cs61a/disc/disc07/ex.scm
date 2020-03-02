; Q1
(define a 1)
(define b a)
(define c 'a)

; Q2
(+ 1)
(* 3)
(+ (* 3 3) (* 4 4))
(define a (define b 3))

; Q3
(if (or #t (/ 1 0)) 1 (/ 1 0))
(if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
((if (< 4 3) + -) 4 100)
(if 0 1 2)

; Q4
; Q4.1
(define (factorial x)
  (if (< x 2) x (* x (factorial (- x 1))))
)

; Q4.2
(define (fib n)
  (if (or (= n 0) (= n 1)) 
    n
    (+ (fib (- n 1)) (fib (- n 2)))
  )
)

; Q5
; Q5.1
(define (concat a b)
  (if (null? a) b (cons (car a) (concat (cdr a) b)))
)
; (concat '(1 2 3) '(4 5 6))
; (1 2 3 4 5 6)

; Q5.2
(define (replicate x n)
  (if (= n 1) (list x) (cons x (replicate x (- n 1))))
)

; Q5.3
(define (cadr l) (car (cdr l)))
(define (uncompress s)
  (if (null? s) nil
  (concat (replicate (car (car s)) (cadr (car s)))
          (uncompress (cdr s))))
)
; (uncompress '((a 1) (b 2) (c 3)))
; (a b b c c c)

; Q5.4
(define (map fn lst)
  (if (null? lst)
    lst
    (cons (fn (car lst)) (map fn (cdr lst))))
)
; (map (lambda (x) (* x x)) '(1 2 3))
; (1 4 9)

(define (deep-map fn lst)
  (cond
    ((null? lst)
      lst)
    ((number? (car lst))
      (cons (fn (car lst)) (deep-map fn (cdr lst))))
    ((pair? (car lst))
      (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
  )
)
; scm> (deep-map (lambda (x) (* x x)) '(1 2 3))
; (1 4 9)
; scm> (deep-map (lambda (x) (* x x)) '(1 ((4) 5) 9))
; (1 ((16) 25) 81)

; Q6
; Q6.1
(define (make-tree label branches) (cons label branches))

(define (label tree) (car tree))

(define (branches tree) (cdr tree))

; Q6.2
(define (sumlst lst) 
  (if (null? lst) 0 (+ (car lst) (sumlst (cdr lst))))
)
(define (is-leaf tree) (null? (branches tree)))
(define (tree-sum tree)
  (if (is-leaf tree) (label tree)
    (+ (label tree) (sumlst (map tree-sum (branches tree))))
  )
)

(define t (make-tree 1 
            (list (make-tree 2
                    (list (make-tree 4 nil) (make-tree 5 nil)))
                  (make-tree 3 nil))))
(tree-sum t)

; Q6.3
(define (helper t previous-root)
  (if (is-leaf t)
      (make-tree (* previous-root (label t)) nil)
      (make-tree (* previous-root (label t))
        (map (lambda (b) (helper b (* previous-root (label t)))) (branches t)))
  )
)
(define (path-product-tree t) (helper t 1))

(define t2 (make-tree 3
            (list (make-tree 0
                    (list (make-tree 10 nil) (make-tree 2 nil)))
                  (make-tree 8 nil)
                  (make-tree -2
                    (list (make-tree -3 nil)))
            )))
(path-product-tree t2)

