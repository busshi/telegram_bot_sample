/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aldubar <aldubar@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/09/13 22:12:56 by aldubar           #+#    #+#             */
/*   Updated: 2021/09/13 22:13:33 by aldubar          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"

int		check_args(char **av)
{
	int	i;

	i = 1;
	while (av[i])
	{
		if (ft_strlen(av[i]) != 9)
			return (0);
		i++;
	}
	return (1);
}

int		check_double(char **av)
{
	int	i;
	int	j;
	int	k;

	i = 1;
	while (av[i])
	{
		j = 0;
		while (av[i][j])
		{
			k = j + 1;
			while (av[i][k])
			{
				if (av[i][j] == av[i][k] && av[i][k] != '.')
					return (0);
				k++;
			}
			j++;
		}
		i++;
	}
	return (1);
}

void	parse(char **av)
{
	int	i;
	int	j;
	int	k;

	i = 1;
	k = 0;
	while (k < 9)
	{
		j = 0;
		while (j < 9)
		{
			if (av[i][j] == '.')
				grid[k][j] = 0;
			else
				grid[k][j] = av[i][j] - '0';
			j++;
		}
		k++;
		i++;
	}
}

int		main(int ac, char **av)
{
    count_sol = 0;
    if (ac == 10 && check_args(av) && check_double(av))
    {
	    parse(av);
	    solver();
	    if (!count_sol)
		    ft_putstr("[KO] Sudoku not solved !!! 🤔\n");
    }
    else
        ft_putstr("Error: bad argument ❌\n");
    return (0);
}
