import { saveAs as saveFile } from 'file-saver';
import { Component, OnInit } from '@angular/core';
import { SubjectService } from '../services/subject.service';
import { AlertsService } from '../services/alerts.service';
import { ActivatedRoute, Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { SequenceViewerComponent } from '../sequence-viewer/sequence-viewer.component';
import { AlignmentViewerComponent } from '../alignment-viewer/alignment-viewer.component';

@Component({
  selector: 'app-assembly',
  templateUrl: './assembly.component.html',
  styleUrls: ['./assembly.component.css']
})
export class AssemblyComponent implements OnInit {

  chrompackId: string;
  subject: string;
  contigs: any;

  constructor(private subjectService: SubjectService,
              private alertService: AlertsService,
              private route: ActivatedRoute,
              private modalService: NgbModal,
              private router: Router) { }

  ngOnInit() {
    this.chrompackId = this.route.snapshot.params['id'];
    this.subject = this.route.snapshot.params['name'];

    this.subjectService.getContigs(this.chrompackId, this.subject).subscribe(
      contigs => this.contigs = contigs,
      err => this.alertService.error("Unable to display the subject's contigs", err)
    );
  }

  download() {
    this.subjectService.downloadFiles(this.chrompackId, this.subject)
    .subscribe(blob => {
      saveFile(blob, `${this.subject}.zip`)
      this.alertService.success('Files downloaded');
    },
    err => {
      this.alertService.error('Assembly result could not be downloaded', err);
    });
  }

  backToSubjects() {
    this.router.navigateByUrl(`chrompack/${this.chrompackId}/subject`);
  }

  backToChrompacks() {
    this.router.navigateByUrl('chrompack');
  }

  viewSequence(contigIndex) {
    const contig = this.contigs[contigIndex];
    const sequence = contig.sequence;
    const name = contig.name;

    const modalRef = this.modalService.open(SequenceViewerComponent);

    modalRef.componentInstance.sequenceLines = sequence;
    modalRef.componentInstance.title = name;
  }

  viewAlignment(contigIndex) {
    const contig = this.contigs[contigIndex];
    let sequenceBase = "";

    contig.sequence.forEach(sequence => { sequenceBase += sequence });

    const modalRef = this.modalService.open(AlignmentViewerComponent);

    modalRef.componentInstance.sequenceBase = sequenceBase;
    modalRef.componentInstance.sequencesToAlign = contig.alignments;
  }
}
