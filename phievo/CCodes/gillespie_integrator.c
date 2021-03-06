
void sum_concentration_embryo(int step, double concentrations[][NCELLTOT]) {

  int g,neig,index,ncell;
  for (ncell=0;ncell<NCELLTOT;ncell++)
  {
    for (g=0;g<SIZE;g++){
      concentrations[g][ncell]=0;
      for (neig=0;neig<NNEIGHBOR;neig++){
	index=geometry[ncell][neig];
	if ((index>=0) && (index!=ncell) ) {
	  concentrations[g][ncell]+=history[g][step][index];
	}
      }
    }
  }
}


double sum_proba(){//computes the sum of probabilities p
  double a0=0;
  int i;
  for (i=0;i<NACTIONS;i++)
    a0+=p[i];

  return a0;

}



int index_next_event(double a){// randomly draws the index of the next mutation
  double mutation=FRAND()*a;
  int index_mutation=0;
  double thresh=0;
  do{
    thresh+=p[index_mutation];
    index_mutation+=1;
  }while(thresh<mutation);
  return index_mutation-1;

}






/* compute the evolution of a system using gillepsie algorithm
*/

void integrator(int kk){

    double s[SIZE][NCELLTOT];
    double sumligands[SIZE][NCELLTOT];
    int index,n,pas,next_event,ncell;
    double t=0;
    double dt=0;
    double a0=0;

    /* initialize geometry here, incase cells move  */
    init_geometry();
    init_history(kk);
    for (n=0;n<NACTIONS;n++)
      p[n]=0.0;

    for (index=0;index<SIZE;index++)
      for (ncell=0;ncell<NCELLTOT;ncell++)
	s[index][ncell] = history[index][0][ncell];


    pas=0;
    do{
      for (ncell=0;ncell<NCELLTOT;ncell++)
	{
	  inputs(pas,ncell,kk);

	  for (index=0;index<NINPUT;index++) {
	    s[trackin[index]][ncell]=history[trackin[index]][pas][ncell];
	  }
	}
       //sum_concentration_embryo(pas,sumligands);  //perform sum of ligands concentrations
	compute_probabilities(s,history,sumligands,pas);
	a0=sum_proba();
	//printf(" %f %i\n",a0,pas);
	if (a0>0){
	  dt=-1.0/a0*log(FRAND());
	  next_event=index_next_event(a0);
	  update_state(s,next_event);
	  t+=dt;
	  if (t>(pas+1)*DT)
	    {
	      pas+=1;
	      for (index=0;index<SIZE;index++)
		for (ncell=0;ncell<NCELLTOT;ncell++)
		  history[index][pas][ncell]= s[index][ncell] ;
	    }
	}
	else	 {

	    t+=DT;
	    pas+=1;
	  }

    }while(pas<NSTEP);

}
