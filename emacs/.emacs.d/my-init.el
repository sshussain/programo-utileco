;; ===== Window frame configuration =====
;; Set window frame size and color in GUI mode
(if (display-graphic-p)
    (progn
      (setq initial-frame-alist
            '(
              (tool-bar-lines . 0)
              (width . 106) ; chars
              (height . 40) ; lines
              (left . 50)
              (top . 50)))
      (setq default-frame-alist
            '(
              (tool-bar-lines . 0)
              (width . 106)
              (height . 60)
              (left . 50)
              (top . 50))))
  (progn
    (setq initial-frame-alist '( (tool-bar-lines . 0)))
    (setq default-frame-alist '( (tool-bar-lines . 0)))))


;; Fonts - default for all modes and all frames
;; (add-to-list 'default-frame-alist '(font . "monospace 14" ))
;; (set-face-attribute 'default t :font "monospace 14" )

;; ==== Packages ====
(require 'package)

;; Use stable packages
(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(add-to-list 'package-archives '("gnu" . "http://elpa.gnu.org/packages/"))  
(add-to-list 'package-archives '("marmalade" . "https://marmalade-repo.org/packages/"))
(add-to-list 'package-archives '("org" . "http://orgmode.org/elpa/") t)

(package-initialize)

;; (setq ido-enable-flex-matching t)
;; (setq ido-everywhere t)
(ido-mode)

(yaml-mode)
