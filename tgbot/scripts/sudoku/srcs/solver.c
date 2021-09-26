/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solver.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aldubar <aldubar@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/09/13 22:14:14 by aldubar           #+#    #+#             */
/*   Updated: 2021/09/13 22:14:42 by aldubar          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"

int		number_unassigned(int *row, int *col)
{
	int		i;
	int		j;

	i = 0;
	while (i < 9)
	{
		j = 0;
		while (j < 9)
		{
			if (grid[i][j] == 0)
			{
				*row = i;
				*col = j;
				return (1);
			}
			j++;
		}
		i++;
	}
	return (0);
}

int		check_horiz(int num, int row)
{
	int		i;

	i = 0;
	while (i < 9)
	{
		if (grid[row][i] == num)
			return (0);
		i++;
	}
	return (1);
}

int		check_vert(int num, int col)
{
	int		i;

	i = 0;
	while (i < 9)
	{
		if (grid[i][col] == num)
			return (0);
		i++;
	}
	return (1);
}

int		check_square(int num, int row, int col)
{
	int		i;
	int		j;

	i = 0;
	while (i < 3)
	{
		j = 0;
		while (j < 3)
		{
			if (grid[(row / 3) * 3 + i][(col / 3) * 3 + j] == num)
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

int		solver(void)
{
	int		row;
	int		col;
	int		num;

	if (!number_unassigned(&row, &col))
	{
		count_sol++;
		ft_putstr("Solution # ");
		ft_putnbr(count_sol);
		ft_putstr("\n");
		print_grid();
	}
	num = 1;
	while (num <= 9)
	{
		if (check_horiz(num, row) && check_vert(num, col)
				&& check_square(num, row, col))
		{
			grid[row][col] = num;
			if (solver())
				return (1);
			grid[row][col] = 0;
		}
		num++;
	}
	return (0);
}
