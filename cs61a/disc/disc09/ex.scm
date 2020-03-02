; Q1
(define (replicate x n)
  (if (= n 0) nil
    (cons x (replicate x (- n 1)))))

(define-macro (repeat-n expr n)
  (cons 'begin (replicate expr n))
)

(repeat-n (print '(resistance is futile)) 4)

; Q2
(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1))
  (if v1 v1 ,expr2))
)

(or-macro (print 'bork) (/ 1 0))
(or-macro (= 1 0) (+ 1 2))

; Q3
(define (prune l state)
  (cond ((null? l) nil)
        (state (prune (cdr l) #f))
        (else (cons (car l) (prune (cdr l) #t)))
  )
)

(define-macro (prune-expr expr)
  (cons (car expr) (prune (cdr expr) #f)) 
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Q2.1
(define (has-even? s)
  (cond ((null? s) #f)
        ((even? (car s)) #t)
        (else (has-even? (cdr-stream s)))))
(define (f x) (* 3 x))
(define nums (cons-stream 1 (cons-stream (f 3) (cons-stream (f 5) nil))))

; Q2.2
(define (range-stream start end)
  (if (= start end) nil
    (cons-stream start (range-stream (+ 1 start) end)))
)
(define s (range-stream 1 5))
(car (cdr-stream s))

; Q2.3
(define (naturals n)
  (cons-stream n (naturals (+ n 1)))
)
(define nat (naturals 0))

(define (slice s start end)
  (cond ((>= start end) nil)
        ((> start 0) (slice (cdr-stream s) (- start 1) (- end 1)))
        ((= start 0) (cons (car s) (slice (cdr-stream s) start (- end 1))))
  )
)

(slice nat 4 12)

; Q2.4
(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
    nil
    (cons-stream
      (f (car xs) (car ys))
      (combine-with f (cdr-stream xs) (cdr-stream ys))))
)

(define integers (naturals 1))
(define factorials
  (cons-stream 1 (combine-with * factorials integers))
)
(slice factorials 0 10)

(define fibs
  (combine-with + (cons-stream -1 (cons-stream 1 fibs)) (cons-stream 1 fibs)))

(slice fibs 0 10)

(define (map-stream f s)
  (cons-stream (f (car s)) (map-stream f (cdr-stream s)))
)

(define (pow x i)
  (if (= i 0) 1
  (* x (pow x (- i 1))))
)

(define (elements x)
  (combine-with / (map-stream (lambda (i) (pow x i)) nat) factorials)
)

(define (exp x)
  (cons-stream (car (elements x)) (combine-with + (cdr-stream (elements x)) (exp x)))
)
