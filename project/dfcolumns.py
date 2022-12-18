#!/usr/bin/env python3
# -*- coding: utf-8 

"""
This module removes excess columns for the dataframe

Module Exports:

remove_columns

"""

def remove_columns(df, column_names):
    """
    This function is used to remove excess columns from dataframe

    Parameters
    ----------
    df : dataframe
    column_names : names of the columns to remove

    Returns:
    -------
    None.

    """
    for i in column_names:
        df.drop(i,axis=1, inplace=True)

