; Macros `check` 29 video 3
(define-macro (check expr) (list 'if expr ''passed 
                                 (list 'quote (list 'failed: expr))))
(define-macro (check expr) `(if ,expr 'passed '(failed: ,expr)))
(check (< 1 0))
(check (> 1 0))

; Macors `for` 29 video 3
(define (map fn vals)
  (if (null? vals)
    ()
    (cons (fn (car vals)) (map fn (cdr vals)))))
(map (lambda (x) (* x x)) '(1 2 3 4))

(define-macro (for sym vals expr)
              (list 'map (list 'lambda (list sym) expr) vals))
(for x '(1 2 3 4) (* x x))
