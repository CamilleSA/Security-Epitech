##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## Makefile
##

all: 
		cp hex_to_base64.py challenge01
		chmod 777 challenge01
		cp fixed_xor.py challenge02
		chmod 777 challenge02
		cp single_byte_xor_cipher.py challenge03
		chmod 777 challenge03
		cp detect_single_byte.py challenge04
		chmod 777 challenge04
		cp implement_repeating_key_xor.py challenge05
		chmod 777 challenge05
		cp break_repeating_key_xor.py challenge06
		chmod 777 challenge06
		cp aes_in_ecb_mode.py challenge07
		chmod 777 challenge07
		cp detect_aes_in_ecb_mode.py challenge08
		chmod 777 challenge08
		cp implement_cbc_mode.py challenge09
		chmod 777 challenge09
		cp byte_at_a_time_ecb_decryption.py challenge10
		chmod 777 challenge10
		cp ecb_cut_and_paste.py challenge11
		chmod 777 challenge11
		cp harder_byte_at_a_time_ecb_decryption.py challenge12
		chmod 777 challenge12
		cp cbc_bitflipping_attacks.py challenge13
		chmod 777 challenge13
		cp the_cbc_padding_oracle.py challenge14
		chmod 777 challenge14

clean: fclean

fclean: 
		rm challenge01
		rm challenge02
		rm challenge03
		rm challenge04
		rm challenge05
		rm challenge06
		rm challenge07
		rm challenge08
		rm challenge09
		rm challenge10
		rm challenge11
		rm challenge12
		rm challenge13
		rm challenge14

re:	fclean all

.PHONY:	all clean fclean re
