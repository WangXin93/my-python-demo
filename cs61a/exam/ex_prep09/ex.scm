; 1. Scheme
; Q1
(define (non-contiguous subseq lst)
  (cond 
    ((null? subseq) #t)
    ((null? lst) #f)
    ((= (car subseq) (car lst)) (non-contiguous (cdr subseq) (cdr lst)))
    (else (non-contiguous subseq (cdr lst)))
  )
)

(non-contiguous '(1 3 6) '(1 2 3 4 5 6))
(non-contiguous '(1 5 2) '(1 2 3 4 5 6))

; yes this procedure is tail recursive

(define (assert-equals expected expression)
  (if (eq? expected (eval expression))
    'OK
    `(expected ,expected but got ,(eval expression))
  )
)

(assert-equals #t '(non-contiguous '(1 3 6) '(1 2 3 4 5 6)))
(assert-equals #f '(non-contiguous '(1 5 2) '(1 2 3 4 5 6)))
(assert-equals #t '(non-contiguous '(1 5 2) '(1 2 3 4 5 6)))

; Q2
(define (directions n sym)
  (define (search s exp)
    ; Search an expresion s for n and return an expression based on exp.
    (cond ((number? s) (if (= s n) exp nil))
          ((null? s) nil)
          (else (search-list s exp))
    )
  )
  (define (search-list s exp)
    ; Search a nested list s for n and return an expression based on exp.
    (let ((first (search (car s) `(car ,exp)))
          (rest (search (cdr s) `(cdr ,exp))))
          (if (null? first) rest first))
  )
  (search (eval sym) sym)
)

(define a '(1 (2 3) ((4))))
(define b '((3 4) 5))

(directions 1 'a) ; (car a)
(directions 2 'a) ; (car (car (cdr a)))
(directions 4 'b) ; (car (cdr (car b)))
(directions 4 'a) ; (car (car (car (cdr (cdr a)))))
(eval (directions 4 'a)) ; 4

; Q3
; (a)
(define days-left 0)
(if (= days-left 0)
  (begin (print 'im-free) 'jk-final)
)

; (b)

; (c)
def do_when_form(vals, env):
    return do_if_form(Pair(vals.first, Pair('begin', vals.second)), env)

; (d)
def do_util_form(vals, env):
    new_expr = Pair(Pair('not', vals.first), vals.second)
    return do_when_form(new_expr, env)

; 2. Stream
(define (reverse-list lst)
  (define (helper lst p)
    (if (null? lst) p
      (helper (cdr lst) (cons (car lst) p)))
  )
  (helper lst nil)
)

(define (stream-to-list s n)
  (define (helper s n lst)
    (if (= n 0) lst
      (helper (cdr-stream s) (- n 1) (cons (car s) lst)))
  )
  (reverse-list (helper s n nil))
)

(define (naturals n)
  (cons-stream n (naturals (+ n 1)))
)
(define ints (naturals 0))
(stream-to-list ints 1000)

(define (list-to-stream lst s)
  (if (null? lst) s
    (cons-stream (car lst) (list-to-strem (cdr lst) s)))
)

(define (cycle-n lst n)
)

(define (cycle lst)
  (define (helper curr-lst)
    (if (null? curr-lst) (helper lst)
      (cons-stream (car curr-lst) (helper (cdr curr-lst))))
  )
  (helper lst)
)
(define a (cycle '(1 2 3)))
(stream-to-list a 100)

(define (stream-first-n n lst)
  (define (stream-helper i curr-lst)
    (cond ((= i 0) (stream-helper n lst))
          ((null? curr-lst) (stream-helper i lst))
          (else (cons-stream (car curr-lst) (stream-helper (- i 1) (cdr curr-lst))))
    )
  )
  (stream-helper n lst)
)
(stream-to-list (stream-first-n 3 '(1 2 3 4)) 10)
(stream-to-list (stream-first-n 7 '(1 2 3 4)) 10)

; 3. Macros
;;;;;;; SCHEME OOP CODE ;;;;;;;;
(define-class Dog)
(define-attr Dog n 'Fido)
(define-attr Dog a 9)
(define-method Dog (age-type)
               (cond
                 ((< (get-attr Dog a) 7) 'young)
                 ((> (get-attr Dog a) 7) 'old)
                 (else 'middle-aged)
                )
)
(define d (construct Dog))
(print (call-method d (age-type)))

;;;;;;; IMPLEMENTATION ;;;;;;;;
(define-macro (define-class class-name)
              `(define ,class-name nil))

(define-macro (construct class-name)
              `(quote ,class-name))

(define-macro (define-attr class-name attr-name value)
              `(define
                 ,class-name
                 (cons
                   '(,attr-name ,(eval value))
                   ,class-name)))

(define-macro (get-attr class-name attr-name)
              `(begin
                 (define (helper class)
                   (if (eq? (quote ,attr-name) (car (car class)))
                     (car (cdr (car class)))
                     (helper (cdr class))))
                 (helper ,class-name)))

(define-macro (define-method class-name signature body)
              `(define-attr ,class-name ,(car signature) (lambda ,(cdr signature) ,body))) 

(define-macro (call-method instance call)
              (cons `(get-attr ,(eval instance) ,(car call)) (cdr call)))
