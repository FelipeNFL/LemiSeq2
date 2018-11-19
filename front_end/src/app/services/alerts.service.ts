import { ToastrService } from "ngx-toastr";
import { Injectable } from "@angular/core";

@Injectable()
export class AlertsService {
    
    constructor(private toastr: ToastrService) {}

    error(msg: string, error=null) {
        this.toastr.error(msg, 'Error', { closeButton: true });

        if(error) {
            console.error(error);
        }
    }

    success(msg: string){
        this.toastr.success(msg, 'Success', { closeButton: true });
    }

    warning(msg: string){
        this.toastr.warning(msg, 'Atention', { closeButton: true });
    }
}