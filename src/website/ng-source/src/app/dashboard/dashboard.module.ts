import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedModule } from '../shared/shared.module';
import { SubstringPipe } from '../shared/pipes';
import { DashboardRoutingModule } from './dashboard-routing.module';

import { DashboardComponent } from './dashboard.component';
import { PluginComponent } from './plugin/plugin.component';
import { SynonymComponent } from './synonym/synonym.component';
import { ProfileComponent } from './profile/profile.component';
import { GroupComponent } from './group/group.component';


@NgModule({
  declarations: [
    DashboardComponent,
    PluginComponent,
    SynonymComponent,
    ProfileComponent,
    GroupComponent,
    SubstringPipe
  ],
  imports: [
    SharedModule,
    CommonModule,
    DashboardRoutingModule
  ],
})
export class DashboardModule {}
