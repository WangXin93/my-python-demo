; Q1
(let ((x 2) (y 5)) (and #f (/ 1 (- x 2))))

(null? (define x '(1 2 3)))

(length ''(cons 1 (cons 2 (cons 3 (cons 4 nil)))))

(append '(1 2 3) '(4 5 6))

(append '(1 2 3) 4)

(cond
  ((pair? x) (cons 5 x))
  ((list? x) (cdr x))
)

(define (caddaadr x)
  (car (cdr (cdr (car (car (cdr x))))))
)

(define x (cons 1 (cons (cons (cons 2 (cons 3 (cons 4 nil))) nil)  nil)))

; Q2
(define (deeval num k)
(cond
  ((and (= k 1) (or (= num 1) (= num 0))) 1)
  ((and (not (= num 1)) (= k 1)) 0)
  (else
    (+ 
      (if (= (modulo num k) 0)
        (deeval (/ num k) (- k 1))
        0
      )
      (deeval (- num k) (- k 1))
    )
  )
)
)
(deeval 1 1) ;1
(deeval 3 2) ;1
(deeval 5 3) ;2

; Q3
; Take two pairs of integers and add them elementwise
(define (pair-add p1 p2)
(cons (+ (car p1) (car p2)) (+ (cdr p1) (cdr p2)))
) 
; Return the length of a list
(define (len lst) 
(if (null? lst) 0
  (+ 1 (len (cdr lst))))
)
(define (cadr lst) (car (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cadddr lst) (car (cdr (cdr (cdr lst)))))

(define (num-calls expr)
  (cond
    ((not (pair? expr)) (cons 1 0))
    ((eq? (car expr) 'if)
     (pair-add
       (num-calls (cadr expr))
       (if (eval (cadr expr))
         (num-calls (caddr expr))
         (num-calls (cadddr expr))
       )
     )
    )
    ((eq? (car expr) 'and)
      (if (null? (cdr expr))
        (cons 0 0)
        (pair-add
          (num-calls (cadr expr))
          (if (not (eval (cadr expr)))
            (cons 0 0)
            (num-calls (caddr expr)))
        )
      )
    )
    ; (else (cons (+ (len expr) 1) 1))
    (else (num-calls-every expr) )
  )
)
(define (num-calls-every expr)
  (if (null? expr) (cons 0 0)
    (pair-add (num-calls (car expr)) (num-calls-every (cdr expr)))
  )
)

(num-calls 1) ;(1 . 0)
(num-calls '(+ 2 2)) ;(4 . 1)
(num-calls '(if #f 3 4)) ;(2 . 0)

; Q4
(define (isset lst)
  (define (helper lst last flag)
    (if (null? lst)
      (if flag #t last)
      (helper 
       (if (= (car lst) last) nil (cdr lst)) 
       (car lst)
       (not (= (car lst) last))
      )
    )
  )
  (helper (cdr lst) (car lst) #t)
)

(define (isset lst)
  (define (helper lst last)
    (cond ((null? lst) #t)
      ((= (car lst) last) last)
      (else (helper (cdr lst) (car lst)))
    )
  )
  (helper (cdr lst) (car lst))
)
(isset '(1 2 3)) ;#t
(isset '(1 2 2 3)) ;2

; Q5
(define (deep-reverse lst)
  (cond
    ((null? lst) lst)
    ((list? (car lst)) 
      (append (deep-reverse (cdr lst)) (cons (deep-reverse (car lst)) nil))
    )
    (else (append (deep-reverse (cdr lst)) (cons (car lst) nil)))
  )
)
(deep-reverse '(foo bar baz))
; (baz bar foo)
(deep-reverse '(1 (2 3) (4 (5 6) 7)))
; ((7 (6 5) 4) (3 2) 1)
