; https://inst.eecs.berkeley.edu/~cs61a/sp18/assets/pdfs/exam_prep09.pdf
(when (> 1 0) 2 3)
; expect 3

(when (< 1 0) 2 3)
; expect f

(when (= 1 1) (+ 2 3) (* 1 2))
; expect 2

(until (< 1 0) 2 3)
; expect 3

(until (> 1 0) 2 3)
; expect #f
