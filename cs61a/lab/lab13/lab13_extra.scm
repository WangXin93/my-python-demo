; Q4
(define (rle s)
  (define (helper curr s)
    (cond
      ((and (null? s) (null? curr)) nil)
      ((null? s) (cons-stream curr nil))
      ((null? curr) (helper (list (car s) 1) (cdr-stream s)))
      ((= (car curr) (car s)) (helper (list (car s) (+ 1 (car (cdr curr)))) (cdr-stream s)))
      (else (cons-stream curr (rle s)))
    )
  )
  (helper nil s)
)


; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

(define s (cons-stream 1 (cons-stream 1 (cons-stream 2 nil))))
(define encoding (rle s))
(stream-to-list (rle (list-to-stream '(1 1 2 2 2 3))))  ; See functions at bottom of lab13.scm


; Q5
(define (inverse-list lst)
  (define (helper head lst)
    (if (null? lst) head
      (helper (cons (car lst) head) (cdr lst))))
  (helper nil lst)
)
(define (insert n s)
  (define (helper front n left)
    (cond
      ((null? left) (inverse-list (cons n front)))
      ((> n (car left)) (helper (cons (car left) front) n (cdr left)))
      (else (append (inverse-list front) (cons n left)))
    )
  )
  (helper nil n s)
)
(insert 1 '(2))
(insert 5 '(2 4 6 8))
(insert 1000 '(1 2 3 4 5 6))

; Q6
(define (deep-map fn s)
  (define (helper head fn s)
    (cond
      ((null? s) head)
      ((list? (car s)) (helper (cons (deep-map fn (car s)) head) fn (cdr s)))
      (else (helper (cons (fn (car s)) head) fn (cdr s)))
    )
  )
  (inverse-list (helper nil fn s))
)
(define (double x) (* 2 x))
(deep-map double '(2 (3 4)))

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (define (helper head lst)
    (if (null? lst) head
      (helper (cons (car lst) head) (filter (lambda (x) (not (eq? x (car lst)))) lst)))
  )
  (inverse-list (helper nil s))
)

(define (count name s)
  (define (helper curr name s)
    (cond
      ((null? s) curr)
      ((eq? name (car s)) (helper (+ 1 curr) name (cdr s)))
      (else (helper curr name (cdr s)))
    )
  )
  (helper 0 name s)
)

(define (tally names)
  (map (lambda (x) (cons x (count x names))) (unique names))
)

(tally '(james jen jemin john))
(tally '(billy billy bob billy bob billy bob))
(tally '())