import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from './dashboard.component';
import { PluginComponent } from './plugin/plugin.component';
import { SynonymComponent } from './synonym/synonym.component';
import { ProfileComponent } from './profile/profile.component';
import { GroupComponent } from './group/group.component';

import { AuthGuard } from '../shared/guards/auth.guard';


const routes: Routes = [
  {path: '', component: DashboardComponent, children: [
    {path: 'plugin', component: PluginComponent, canActivate: [AuthGuard]}, 
    {path: 'synonym', component: SynonymComponent, canActivate: [AuthGuard]},
    {path: 'profile', component: ProfileComponent, canActivate: [AuthGuard]}, 
    {path: 'group', component: GroupComponent, canActivate: [AuthGuard]}, 
  ]}
];
@NgModule({
  imports: [
    RouterModule.forChild(routes),
  ],
  exports: [
    RouterModule
  ]
})
export class DashboardRoutingModule {
  
}
