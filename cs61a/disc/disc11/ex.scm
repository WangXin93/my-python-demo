; 4.1
(define-macro (do-when-form condition exprs)
  `(if ,condition ,(cons 'begin exprs)  'okay)
)

(define-macro (do-when-form condition exprs)
  (list 'if condition (cons 'begin exprs) 'okay)
)

(do-when-form (= 1 0) ((/ 1 0) 'error))
(do-when-form (= 1 1) ((print 61) (print 'a) 'final-review))

; 5.1
(define (range start step)
  (cons-stream start (range (+ start step) step)))
(define (stream-to-list s end)
  (if (<= end 0) (list (car s))
  (cons (car s) (stream-to-list (cdr-stream s) (- end 1))))
)

(define integers (range 1 1))
(define odds (range 1 2))
(define evens (range 0 2))

(define (merge s1 s2)
  (if (< (car s1) (car s2))
         (cons-stream (car s1) (merge (cdr-stream s1) s2))
         (cons-stream (car s2) (merge s1 (cdr-stream s2)))
  )
)
(stream-to-list (merge odds evens) 10)

; 5.2
(define (cycle start)
  (cons-stream (if (>= start 5) (remainder start 5) start) (cycle (+ start 2))))
(stream-to-list (cycle 1) 10)

