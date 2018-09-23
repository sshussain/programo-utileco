
;; Do not show startup splash message
(setq inhibit-startup-message t)

;; ===== Key Mapping ======
;; Set modifier key map of MacOS
(when (eq system-type 'darwin) ;; mac specific settings
  (global-set-key [kp-delete] 'delete-char) ;; sets fn-delete to be right-delete
;  (setq mac-option-modifier 'alt)
;  (setq mac-command-modifier 'meta)
)

;; Global key mapping - independent of major or minor modes
(global-set-key "\C-x\C-b" 'electric-buffer-list)
(global-set-key (kbd "<f2>") 'beginning-of-buffer)    ; go to first line
(global-set-key (kbd "<f3>") 'end-of-buffer)    ; go to last line
(global-set-key (kbd "<f4>") 'goto-line)        ; go to line

;; ===== Indentation and tabbing ======
(setq-default standard-indent 4)
(setq-default tab-width 4)
(setq-default indent-tabs-mode nil) ;; turn-on tab character

;; ==== Display -- tool bar, menu, fringes, ...
(menu-bar-mode -1) ; disable menu bar
(tool-bar-mode -1) ; disable tool bar
;; (fringe-mode 0)
; (global-hl-line-mode 1) ; highlight line that contains the cursor. Looks bad with certain dark themes
;; Disable line numbers to unclutter display
; (global-display-line-numbers-mode) ; show line numbers

;; ===== Mouse navigation =====
(mouse-wheel-mode t) ; mouse wheel scrolling

;; ===== Backup and Save =====
(setq make-backup-files nil) ; stop creating backup~ files
(setq auto-save-default nil) ; stop creating #autosave# files

(setq default-major-mode 'text-mode) ; set default mode to text

;; Load my customization
(load-file "~/.emacs.d/my-init.el")

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["#2e3436" "#a40000" "#4e9a06" "#c4a000" "#204a87" "#5c3566" "#729fcf" "#eeeeec"])
 '(custom-enabled-themes (quote (wheatgrass)))
 '(custom-safe-themes
   (quote
    ("21d9280256d9d3cf79cbcf62c3e7f3f243209e6251b215aede5026e0c5ad853f" "41576d31aa4aba50b68c66bc186c4a756241e0745ad4d7ff0e25ecbc21642c0b" "40da996f3246a3e99a2dff2c6b78e65307382f23db161b8316a5440b037eb72c" "787574e2eb71953390ed2fb65c3831849a195fd32dfdd94b8b623c04c7f753f0" "037be823f630fada7f90028b1a6b3745e288436db649ae783d008fe0c1d98cff" "6c5a5c47749e7992b4da3011595f5470f33e19f29b10564cd4f62faebbe36b91" "a8c595a70865dae8c97c1c396ae9db1b959e86207d02371bc5168edac06897e6" "76dc63684249227d64634c8f62326f3d40cdc60039c2064174a7e7a7a88b1587" default)))
 '(electric-indent-mode t)
 '(electric-layout-mode t)
 '(package-selected-packages
   (quote
    (tango-2-theme yaml-mode pastelmac-theme greymatters-theme atom-dark-theme json-mode)))
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Courier New" :foundry "outline" :slant normal :weight normal :height 102 :width normal)))))
(put 'downcase-region 'disabled nil)
(put 'upcase-region 'disabled nil)

(load-theme 'nord)
