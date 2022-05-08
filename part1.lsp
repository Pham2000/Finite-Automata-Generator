;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  ;;Description: This is a hard coded lisp program, that take in
  ;;a list of characters and tell whether or not they are illegal,
  ;;this program is hard coded to only accept theString.txt.
  ;;Author: Tri Pham
  ;;Course: COP4020
  ;;Project number: 04
  ;;Date: 04/15/2022
  ;;File Name: part1.lsp
  ;;Version 0.720
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun demo()
	(setq fp (open "theString.txt" :direction :input))
	(setq l (read fp "done"))
	(princ "processing ")
	(princ l)
	(fsa l)
)

(defun fsa(l)
	(state0 l)
)

(defun state0(l)
	(COND
		((null l) "illegal")
		((equal 'x (car l)) (state0 (cdr l)))
		((equal 'y (car l)) (state1 (cdr l)))
		(T "illegal character at state 0")
	)	
)

(defun state1(l)
	(COND
		((null l) "legal")
		((equal 'x (car l)) (state2 (cdr l)))
		(T "illegal character at state 1")
	)
)

(defun state2(l)
	(COND
		((null l) "illegal")
		((equal 'x (car l)) (state2 (cdr l)))
		((equal 'y (car l)) (state3 (cdr l)))
		(T "illegal character at state 2")
	)
)

(defun state3(l)
	(COND
		((null l) "legal")
		((equal 'x (car l)) (state3 (cdr l)))
		((equal 'z (car l)) (state4 (cdr l)))
		(T "illegal character at state 3")	
	)	
)

(defun state4(l)
	(COND
		((null l) "illegal")
		((equal 'x (car l)) (state4 (cdr l)))
		((equal 'a (car l)) (state1 (cdr l)))
		(T "illegal character at state 4")	
	)
)
