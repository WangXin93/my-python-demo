(define x 1)

(define p (delay (+ x 1)))

p

(force p)

(define (foo x) (+ x 10))

(define bar (cons-stream (foo 1)
             (cons-stream (foo 2) bar)))

(car bar)

(cdr bar)

(define (foo x) (+ x 1))

(cdr-stream bar)

(define (foo x) (+ x 5))

(car bar)

(cdr-stream bar)

; Code Writing for Streams
; Q1
(define (double-naturals)
  (double-naturals-helper 1 #f)
)
(define (double-naturals-helper first go-next)
  (if go-next
    (cons-stream first (double-naturals-helper (+ first 1) #f))
    (cons-stream first (double-naturals-helper first (not go-next)))
  )
)

(define (slice s start end)
   (cond ((>= start end) nil)
         ((> start 0) (slice (cdr-stream s) (- start 1) (- end 1)))
         ((= start 0) (cons (car s) (slice (cdr-stream s) start (- end 1))))
   )
)

; Q2
(define (naturals n)
  (cons-stream n (naturals (+ n 1)))
)
(define nat (naturals 0))

(define (interleave stream1 stream2)
  (cons-stream (car stream1)
    (cons-stream (car stream2)
      (interleave (cdr-stream stream1) (cdr-stream stream2))
    )
  )
)

(define double-nat (interleave nat nat))
(slice double-nat 0 10)
