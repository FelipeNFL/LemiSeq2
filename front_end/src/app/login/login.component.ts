import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../services/auth.service';
import { AlertsService } from '../services/alerts.service';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';

@Component({
    selector: 'login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent {

    loading: boolean = false;
    _usernameModel: string;
    _passwordModel: string;

    constructor(private authService: AuthService,
                private alerts: AlertsService,
                private router: Router,
                private chrompackServiceObservable: ChrompackServiceObservable) { }
    
    login(){
        this.loading = true;

        this.authService.requestToken(this._usernameModel, this._passwordModel).subscribe(
        data => { 
            this.authService.setSession(data.token, data.fullname);
            this.loading = false;
            this.router.navigate(['/plate']);
            this.chrompackServiceObservable.sendRefreshResult();
        },
        err => {
            this.loading = false;              
            this.alerts.error("Do not possible to do login. Contact the administrator", err);
        });
    }
}