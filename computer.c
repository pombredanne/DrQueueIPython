/* $Id: computer.c,v 1.1 2001/05/07 15:35:04 jorge Exp $ */

#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>

#include "computer.h"
#include "database.h"

int computer_index_addr (void *pwdb,struct in_addr addr)
{
  int index;
  struct hostent *host;
  char *dot;
  int i=0;

  host = gethostbyaddr (&addr,sizeof (struct in_addr),AF_INET);
  if ((dot = strchr (host->h_name,'.')) != NULL) 
    *dot = '\0';
  printf ("Name: %s\n",host->h_name);
  while (host->h_aliases[i] != NULL) {
    printf ("Alias: %s\n",host->h_aliases[i]);
    i++;
  }
  while (*host->h_aliases != NULL) {
    printf ("Alias: %s\n",*host->h_aliases);
    host->h_aliases++;
  }

  index = computer_index_name (pwdb,host->h_name);

  printf ("Index %i\n", index);

  return index;
}

int computer_index_name (void *pwdb,char *name)
{
  struct database *wdb = (struct database *)pwdb;
  int index = -1;
  int i;
  
  for (i=0;((i<MAXCOMPUTERS)&&(index==-1)); i++) {
    if (strcmp(name,wdb->computer[i].hwinfo.name) == 0)
      index = i;
  }

  return index;
}

int computer_index_free (void *pwdb)
{
  /* Return the index to a free computer record OR -1 if there */
  /* are no more free records */
  int index = -1;
  int i;
  struct database *wdb = (struct database *)pwdb;

  for (i=0; i<MAXCOMPUTERS; i++) {
    if (wdb->computer[i].used == 0) {
      index = i;
      break;
    }
  }

  return index;
}



