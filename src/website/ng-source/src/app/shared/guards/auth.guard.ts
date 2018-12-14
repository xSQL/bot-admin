import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';

import { UserService } from '../services/user.service'; 
 
@Injectable()
export class AuthGuard implements CanActivate {
 
    constructor(private router: Router, private userService: UserService) { }
 
    canActivate() {
      let response = this.userService.verify();
      if(!response) {
        this.router.navigate(['/auth/login']);
      }
      return response;
    }
}
