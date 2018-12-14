import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthComponent } from './auth/auth.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { AuthGuard } from './shared/guards/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/group', pathMatch: 'full' },
  { path: 'auth', component: AuthComponent},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {
  
}
