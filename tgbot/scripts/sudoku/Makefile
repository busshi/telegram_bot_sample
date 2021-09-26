# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aldubar <aldubar@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/13 22:15:23 by aldubar           #+#    #+#              #
#    Updated: 2021/09/13 22:19:28 by aldubar          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SRCS	= srcs/main.c srcs/ft_ft.c srcs/solver.c srcs/print.c

OBJS	= $(SRCS:.c=.o)

HEADER	= includes

NAME	= sudoku_solver

CC		= @clang

CFLAGS	= -Wall -Wextra -Werror

RM		= @rm -f

$(NAME):
	$(CC) $(CFLAGS) $(SRCS) -I$(HEADER) -o $(NAME)

all:	$(NAME)

clean:
	$(RM) $(OBJS)

fclean:		clean
	$(RM) $(NAME)

re:		fclean all

.PHONY:	all clean fclean re
