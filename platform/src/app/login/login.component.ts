import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { HttpErrorResponse } from '@angular/common/http';
import { AuthService } from '../services/auth.service';

@Component({
    selector: 'login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent {

    messageError: string = null;
    _usernameModel: string;
    _passwordModel: string;

    constructor(private authService: AuthService,
                private router: Router) { }
    
    login(){

        this.authService.requestToken(this._usernameModel, this._passwordModel).subscribe(
            (data) => { 
                this.authService.setSession(data.token, data.fullname);
                this.router.navigate(['/upload']);
            },
            (errorResponse: HttpErrorResponse) => { 
                this.messageError = errorResponse.error;
            }
        );
    }
}