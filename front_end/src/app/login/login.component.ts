import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { HttpErrorResponse } from '@angular/common/http';
import { AuthService } from '../services/auth.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';

@Component({
    selector: 'login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent {

    messageError: string = null;
    loading: boolean = false;
    _usernameModel: string;
    _passwordModel: string;

    constructor(private authService: AuthService,
                private router: Router,
                private chrompackServiceObservable: ChrompackServiceObservable) { }
    
    login(){

        this.loading = true;

        this.authService.requestToken(this._usernameModel, this._passwordModel).subscribe(
            (data) => { 
                this.authService.setSession(data.token, data.fullname);
                this.loading = false;
                this.router.navigate(['/plate/upload']);
                this.chrompackServiceObservable.sendRefreshResult();
            },
            (errorResponse: HttpErrorResponse) => {
                this.loading = false;                 
                this.messageError = errorResponse.error;
            }
        );

    }
}