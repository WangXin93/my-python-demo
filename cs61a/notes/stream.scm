(define (map-stream f s)
 (if (null? s)
  (cons-stream (f (car s))
   (map-stream (cdr-stream s))))
 )


(define (filter-stream f)
 (if (null? s)
  nil
  (if (f (car s))
   (cons-stream (car s) (filter-stream f (cdr-stream s)))
   (filter-stream f (cdr-stream s))))
 )

(define (reduce-stream f s start)
 (if (null? s)
  start
  (reduce-stream f
   (cdr-stream s)
   (f start (car s))))
 )

(define (sieve s)
 (cons-stream (car s)
  (sieve
  (filter-stream (lambda (x) (not (= 0 (remainder x (car s))))
                  (cdr-stream s)))
  )))
